var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');
var handlebars = require('handlebars');

var TodoCollection = require('../Collection/TodoCollection.js');
var TodoModel = require('../Model/TodoModel.js');

var todoViewTemplate = require('../templates/todo.hbs');


var TodoView = Backbone.View.extend({
    tagName: 'li',
    events: {},

    initialize: function(){
        // this.todo = new TodoModel();
        this.render();
    },

    render: function(){
        var todo = this.model.toJSON();
        this.el.innerHTML = todoViewTemplate({subject: todo.subject});
    }
})

module.exports = TodoView;
