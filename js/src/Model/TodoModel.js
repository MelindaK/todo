var Backbone = require('backbone');

var TodoModel = Backbone.Model.extend({
    urlRoot: 'todos/',
    defaults: {
        subject: 'Subject',
        dueDate: null,
        description: '',
        priority: null,
        completed: false,
        assignee: null,
    },
    parse: function(response, options){
        if (options.collection) {
            return response;
        }
        return response.result;
    }
})

module.exports = TodoModel;
