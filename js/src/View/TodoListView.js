var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');
var handlebars = require('handlebars');

var TodoListCollection = require('../Collection/TodoListCollection.js');
var TodoListModel = require('../Model/TodoListModel.js');

var todoListViewTemplate = require('../templates/todolist.hbs');


var TodoListView = Backbone.View.extend({
    //why does $ syntax not work here

    el: '.todo-lists-container',

    events: {},

    initialize: function(){
        this.todoLists = new TodoListCollection();
        this.todoLists.fetch({
            success: _.bind(function(model){
                console.log('Success: todoLists loaded.');
                this.render();
            }, this),
            error: function(){
                console.log('Error: todolists failed to load.');
            }
        });
    },

    render: function(){
        this.todoLists.each(function(todoList){
            this.el.innerHTML = todoListViewTemplate({listName: todoList.get('name')});
        }, this)
    }
})

module.exports = TodoListView;
