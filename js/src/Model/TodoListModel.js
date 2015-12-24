var Backbone = require('backbone');
// var TodoListCollection = require('../Collection/TodoListCollection.js')

var TodoListModel = Backbone.Model.extend({
    urlRoot: '/todolists',
    defaults: {
        name: 'List Name',
        creator: 'User'
    },
    parse: function(response, options){
        if (options.collection) {
            return response;
        }
        return response.result;
    }
})

module.exports = TodoListModel;
