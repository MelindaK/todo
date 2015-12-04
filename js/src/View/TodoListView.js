var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');
var handlebars = require('handlebars');

var TodoListModel = require('../Model/TodoListModel.js');
var TodoModel = require('../Model/TodoModel.js');
var TodoListCollection = require('../Collection/TodoListCollection.js');
var TodoCollection = require('../Collection/TodoCollection.js');
var TodoView = require('./TodoView.js')


var todoListViewTemplate = require('../templates/todolist.hbs');


var TodoListView = Backbone.View.extend({
    //why does $ syntax not work here?

    tagName: 'div',
    className: 'todo-list-container',

    events: {},

    initialize: function(){
        // create todoList model
        this.renderTodoList();

        // create todo collection
        this.todos = new TodoCollection([], {id: this.model.id});
        this.todos.fetch({
            success: _.bind(function(model){
                console.log('Success: Todos loaded.');
                this.renderTodos();
            }, this),
            error: function(){
                console.log('Error: Todos failed to load.');
            }
        })


    },

    renderTodoList: function(){
        var todoList = this.model.toJSON();
        this.el.innerHTML = todoListViewTemplate({listName: todoList.name});

    },

    renderTodos: function(){
        this.todos.each(function(todo){
            var todoView = new TodoView({
                model: todo
            })
            this.el.querySelector('ul').appendChild(todoView.el)
        }, this)
    }
})

module.exports = TodoListView;
