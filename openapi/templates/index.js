const py = module.exports;
const fs = require("fs");
const _ = require("lodash");

py.process = ({ spec, operations, models, handlebars }) => {
  py.spec = spec;
  const templates = [];
  const modelsByName = [];

  // Model Name -> Model Object mapping
  for (let model of models) {
    modelsByName[model.modelName] = model;
  }

  for (let model of models) {
    if (model.extends !== undefined) {
      // Get Resolution from parent
      model.parent = modelsByName[model.extends];
      if (
        model.parent.resolutionStrategy !== undefined &&
        model.parent.parent == undefined
      ) {
        for (let value in model.parent.resolutionStrategy.valueToModelMapping) {
          if (model.modelName)
            if (
              model.parent.resolutionStrategy.valueToModelMapping[value] ===
              model.modelName
            ) {
              model.resolution = {
                fieldName: model.parent.resolutionStrategy.propertyName,
                fieldValue: value,
              };
            }
        }
      }
      if (
        model.parent.parent !== undefined &&
        model.parent.parent.resolutionStrategy !== undefined
      ) {
        model.resolution = model.parent.resolution;
      }
    }

    if (model.enum) {
      if (model.type === "integer") model.type = "int";
      if (model.type === "string") model.type = "str";
      if (!model.type) model.type = "str";
    }

    templates.push({
      src: "model.py.hbs",
      dest: `okta/models/${_.snakeCase(model.modelName)}.py`,
      context: {
        model: model,
        subTypes: getSubtypes(model),
      },
    });
  }

  // get operations
  let clientOps = {};
  for (let operation of operations) {
    let tag = operation.tags[0];
    if (tag === "AuthServer") tag = "AuthorizationServer";
    if (tag === "Template") tag = "SmsTemplate";
    if (tag === "Idp") tag = "IdpTrust";
    if (tag === "UserFactor") tag = "UserFactor";
    if (tag === "Log") tag = "LogEvent";

    if (_.has(clientOps, tag)) {
      clientOps[tag].push(operation);
    } else {
      clientOps[tag] = [operation];
    }
  }

  for (const [tag, ops] of Object.entries(clientOps)) {
    templates.push({
      src: "resource_client.py.hbs",
      dest: `okta/resource_clients/${_.snakeCase(tag)}_client.py`,
      context: {
        operations: ops,
        resource: tag,
      },
    });
  }

  templates.push({
    src: "client.py.hbs",
    dest: `okta/client.py`,
    context: {
      resources: Object.keys(clientOps),
    },
  });

  templates.push({
    src: "models-init.py.hbs",
    dest: `okta/models/__init__.py`,
    context: {
      models: models,
    },
  });

  handlebars.registerHelper({
    operationArgumentBuilder,
    pyDocstringBuilder,
    updatePath,
    displayMethodName,
    multilineURL,
    importURLEncode,
    getResourceImports,
    hasBinaryOps,
    replaceColons,
    returnsApplication
  });

  handlebars.registerPartial(
    "partials.copyrightHeader",
    fs.readFileSync("openapi/templates/partials/copyrightHeader.hbs", "utf8")
  );
  handlebars.registerPartial(
    "partials.defaultMethod",
    fs.readFileSync(
      "openapi/templates/partials/models/defaultMethod.py.hbs",
      "utf8"
    )
  );

  return templates;
};

/* Helper functions */

// Returns if method is POST or PUT for operation
function isPostOrPut(method) {
  return method === "post" || method === "put";
}

/* Handlebars helpers */

// Write out parameters for operation
function operationArgumentBuilder(operation) {
  let args = ["self"];
  operation.pathParams.map((param) => args.push(param.name));

  // check body model if required with request
  if (operation.bodyModel && isPostOrPut(operation.method)) {
    let bodyModel = _.snakeCase(operation.bodyModel);
    args.push(bodyModel);
  }

  if (operation.queryParams.length) {
    args.push("query_params={}");
  }
  return args.join(", ");
}

// Write out docstring for operation
function pyDocstringBuilder(method) {
  const docs = [];

  const ONE_TAB = " ".repeat(8);
  const TWO_TABS = ONE_TAB + " ".repeat(4);

  let descString = method.description || `Method for\n${method.path}`;
  descString.match(/.{1,55}/g).forEach((line) => {
    if (!line.toLowerCase().includes("success")) {
      docs.push(`${ONE_TAB}${line.trim()}`);
    }
  });

  docs.push(`${ONE_TAB}Args:`);
  if (method.pathParams.length) {
    method.pathParams
      .map((param) => {
        return `${TWO_TABS}${_.snakeCase(param.name)} {str}`;
      })
      .forEach((doc) => docs.push(doc));
  }

  if (!method.isArray && method.bodyModel) {
    docs.push(`${TWO_TABS}{${_.snakeCase(method.bodyModel)}}`);
  }

  if (method.queryParams.length) {
    docs.push(
      `${TWO_TABS}query_params {dict}: Map of query parameters for request`
    );
    method.queryParams
      .map((param) => {
        return `${TWO_TABS}[query_params.${param.name}] {str}`;
      })
      .forEach((queryParam) => docs.push(queryParam));
  }

  if (method.responseModel) {
    docs.push(`${ONE_TAB}Returns:`);
    if (method.isArray) {
      docs.push(
        `${TWO_TABS}list: Collection of ${method.responseModel} instances.`
      );
    } else {
      docs.push(`${TWO_TABS}${method.responseModel}`);
    }
  }

  return docs.join("\n");
}

// Write out path for operation
function updatePath(operation) {
  let result = operation.path;
  if (operation.pathParams.length) {
    operation.pathParams.forEach((param) => {
      result = result.replace(param, { param });
    });
    result = multilineURL(result);
  }
  return result;
}

// Helper function to split URL into multiple lines
function multilineURL(path) {
  let pieces = path.split("/").filter((segment) => {
    return segment.length > 0;
  });
  let result = [];
  let current = "";
  const LIMIT = 50;

  pieces.forEach((piece) => {
    if (piece.length + current.length <= LIMIT) {
      current = current.concat(`/${piece}`);
    } else {
      result.push(current);
      current = `/${piece}`;
    }
  });

  result.push(current);
  return result.join(`\n${" ".repeat(16)}`);
}

// Shorten operation names which were too long
function displayMethodName(name) {
  const LONG_WORDS = {
    application: "app",
    administrator: "admin",
  };
  if (name.length > 60) {
    for (let key in LONG_WORDS) {
      name = name.replace(key, LONG_WORDS[key]);
    }
  }

  return name;
}

// check if resource client has an operation with query parameters
// indicates if URLEncoder should be imported
function importURLEncode(operations) {
  return (
    operations.filter((operation) => {
      return operation.queryParams.length > 0;
    }).length > 0
  );
}

// Import all datatypes used in resource client
function getResourceImports(operations) {
  let result = new Set();
  for (let op of operations) {
    if (op.responseModel) {
      result.add(op.responseModel);
    }
  }
  return [...result];
}

// If resource client has any binary operations
function hasBinaryOps(operations) {
  return (
    operations.filter((operation) => {
      return operation.bodyFormat === "binary";
    }).length > 0
  );
}

// Replace colons in enums with underscores
function replaceColons(modelName) {
  return modelName.replace(/:/g, "_");
}

// Import subtypes in models
function getSubtypes(model) {
  let modelSubTypes = new Set();

  if (model.properties) {
    model.properties.forEach((prop) => {
      if ("$ref" in prop) {
        modelSubTypes.add(prop.model);
      }
    });
  }

  return [...modelSubTypes];
}

function returnsApplication(operations) {
  return (
    operations.filter((operation) => {
      return _.lowerCase(operation.responseModel) === "application";
    }).length > 0
  );
}
