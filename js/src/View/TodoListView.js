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

    events: {
        'click .deleteList': 'deleteList',
        'keypress .todo': 'addTodoKeyPress',
        'click .addTodo': 'addTodoClick',
        'keypress .listName': 'updateList',
    },

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
    },

    deleteList: function(){
        this.model.destroy();
        this.el.parentNode.removeChild(this.el);
    },

    _addTodo: function(){
        var todoListId = this.model.id;

        var newTodo = new TodoModel({
            subject: 'subject',
            todoListId: todoListId
        })

        newTodo.save(null, {
            success: _.bind(function(model) {
                console.log('Success: todo created.');

                this.todos.add(newTodo);
                var todoView = new TodoView({
                    model: newTodo
                })
                this.el.querySelector('ul').appendChild(todoView.el);
                this.el.querySelector('ul li:last-child input.todo').focus();
            }, this),
            error: function(){
                console.log('Error: todo not created.');
            }
        })
    },

    addTodoKeyPress: function(e){
        var code = e.keyCode;
        var lastItem = this.el.querySelector('ul li:last-child input.todo');
        if (code === 13 && e.currentTarget === lastItem) {
            this._addTodo();
        }
    },

    addTodoClick: function(){
        this._addTodo();
    },

    updateList: function(e){
        var code = e.keyCode;
        var newListName = e.currentTarget.value;

        if (code === 13) {
            this.model.save({'name': newListName})
            e.currentTarget.blur();
        }
    },
})

module.exports = TodoListView;
