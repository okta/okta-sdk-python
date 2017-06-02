const _ = require('lodash');

const python = module.exports;
/**
 * This file is used by the @okta/openapi generator.  It defines language-specific
 * post-processing of the JSON spec, as well as handebars helpers.  This file is meant
 * to give you control over the data that handlebars uses when processing your templates
 */

python.process = ({spec, operations, models, handlebars}) => {

  // A map of operation Id's do their definition, so that
  // we can reference them when building out methods for x-okta-links

  // Collect all the operations

  const templates = [];

  templates.push({
	src: 'api_client.py.hbs',
	dest: 'api_client.py',
    context: {operations}
  });

  //add all the models
  for (let model of models) {
    for (let property of model.properties) {
      switch (property.model) {
        case 'object':
          // To accomodate for unspecified hashes
          property.model = 'OktaObject';
          break;
        case 'array':
        case 'boolean':
        case 'string':
          delete property.model;
      }
    }

    templates.push({
      src: 'models.py.hbs',
      dest: `models/${_.snakeCase(model.modelName)}.py`,
      context: model
    });

    templates.push({
      src: 'models.index.py.hbs',
      dest: 'models/__init__.py',
      context: { models }
    });
  }

  // Add helpers
  const paramMatcher = /{(.*?)}/g;
  handlebars.registerHelper('replacePathParams', (path) => {
    // Everywhere there's a {id}, replace it with {opts.id}
    if (paramMatcher.test(path)) {
      const matches = path.match(paramMatcher);
      for (let match of matches) {
        const param = match.slice(1);
        path = path.replace(match, `{}`);
      }
    }
    return path;
  });

  handlebars.registerHelper('retrievePathParams', (path) => {
    // Everywhere there's a {id}, return it in an array
    if (paramMatcher.test(path)) {
      const matches = path.match(paramMatcher);
      const newMatches = [];
      for (let match of matches) {
      	newMatches.push(_.snakeCase(match.replace('{', '').replace('}', '')));
      }
      return ".format(" + newMatches.join(', ') + ")";
    }
  });

  handlebars.registerHelper('operationArgumentBuilder', (operation) => {

    const args = ['self'];

    operation.pathParams.map((arg) => args.push(_.snakeCase(arg.name)));

    if ((operation.method === 'post' || operation.method === 'put') && operation.bodyModel) {
      args.push(_.snakeCase(operation.bodyModel));
    }

    if (operation.queryParams.length) {
      args.push('**kwargs');
    }

    return args.join(', ');
  });

  handlebars.registerHelper('snakeCase', (word) => {
    return _.snakeCase(word);
  });

  return templates;
};
