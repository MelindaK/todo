var Backbone = require('backbone');

var TodoModel = Backbone.Model.extend({
    defaults: {
        subject: 'Subject',
        dueDate: 'Due date',
        description: '',
        priority: null,
        completed: false,
        assignee: null,
    }
})

module.exports = TodoModel;
