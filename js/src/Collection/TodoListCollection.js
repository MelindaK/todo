var Backbone = require('backbone');

var TodoListModel = require('../Model/TodoListModel.js');

var TodoListCollection = Backbone.Collection.extend({
    model: TodoListModel,
    url: '/todolists',
    parse: function(response){
        return response.result;
    }
})

module.exports = TodoListCollection;
