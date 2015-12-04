var Backbone = require('backbone');

var TodoModel = require('../Model/TodoModel.js');

var TodoCollection = Backbone.Collection.extend({
    initialize: function(models, options){
        this.id = options.id
    },
    model: TodoModel,
    url: function(){
        return '/todos?todoListId=' + this.id;
    },
    parse: function(response){
        return response.result;
    }
})

module.exports = TodoCollection;
