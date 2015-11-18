var Backbone = require('backbone');

var TodoListModel = require('../Model/TodoListModel.js');

var TodoListCollection = Backbone.Collection.extend({
    model: TodoListModel,
    url: '/todolists',
    parse: function(response){
        // var models = [];
        // for(var i = 0; i < response.result.length; i++){
        //     var newModel = new TodoListModel({
        //         id: response.result[i].id,
        //         creator: response.result[i].creator,
        //         name: response.result[i].name
        //     });
        //     models.push(newModel);
        // }
        return response.result;
    }
})

module.exports = TodoListCollection;
