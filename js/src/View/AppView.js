var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');
var handlebars = require('handlebars');

var UserModel = require('../Model/UserModel.js');
var appViewTemplate = require('../templates/container.hbs');
var TodoListView = require('./TodoListView.js');

var AppView = Backbone.View.extend({
    el: 'body',
    events: {},

    initialize: function(){
        // access user model (get logged-in user name)
        // Also we need a loggin screen
        this.user = new UserModel();
        this.user.fetch({
            success: _.bind(function(model){
                console.log('Success: user loaded.');
                this.render();
                var todoListView = new TodoListView();
            }, this),
            error: function(){
                console.log('Error: user failed to load.');
            }
        })
    },

    render: function(){

        this.el.innerHTML = appViewTemplate({userName: this.user.get('name')});
    }
})

module.exports = AppView;
