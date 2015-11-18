var Backbone = require('backbone');

var TodoListModel = Backbone.Model.extend({
    defaults: {
        name: 'List Name',
        creator: 'User'
    }
})

module.exports = TodoListModel;
