var Backbone = require('backbone');

var TodoListModel = Backbone.Model.extend({
    url: '/todolists',
    defaults: {
        name: 'List Name',
        creator: 'User'
    }
})

module.exports = TodoListModel;
