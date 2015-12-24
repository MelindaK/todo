var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');
var handlebars = require('handlebars');

var UserModel = require('../Model/UserModel.js');
var appViewTemplate = require('../templates/container.hbs');
var TodoListView = require('./TodoListView.js');
var TodoListCollection = require('../Collection/TodoListCollection.js');
var TodoListModel = require('../Model/TodoListModel.js');
var todoAppTemplate = require('../templates/todoapp.hbs');

var AppView = Backbone.View.extend({
    el: 'body',
    events: {
        'click .addlist': 'addNewList',
    },

    initialize: function(){

        this.render();

        this.user = new UserModel();
        this.user.fetch({
            success: _.bind(function(model){
                console.log('Success: user loaded.');
                this.renderUser();
            }, this),
            error: function(){
                console.log('Error: user failed to load.');
            }
        })

        this.todoLists = new TodoListCollection();
        this.todoLists.fetch({
            success: _.bind(function(model){
                console.log('Success: todoLists loaded.');
                this.renderTodoLists();
            }, this),
            error: function(){
                console.log('Error: todolists failed to load.');
            }
        });
    },

    render: function(){
        this.el.insertAdjacentHTML('afterbegin', todoAppTemplate({}));
    },

    renderUser: function(){
        this.el.querySelector('.user-container').innerHTML = appViewTemplate({userName: this.user.get('name')});

    },

    renderTodoLists: function(){
        this.todoLists.each(function(todoList, i){
            var todoListView = new TodoListView({
                model: todoList
            })
            this.el.querySelector('.todo-lists-container').appendChild(todoListView.el)
        }, this)
    },

    addNewList: function(){
        var newList = new TodoListModel({
            name: "name",
        })

        newList.save(null, {
            success: _.bind(function(model) {
                console.log('Success: todoList created.');

                this.todoLists.add(newList);
                var todoListView = new TodoListView({
                    model: newList
                })
                this.el.querySelector('.todo-lists-container').appendChild(todoListView.el)
            }, this),
            error: function(){
                console.log('Error: todolists not created.');
            }
        });
    },

})

module.exports = AppView;
