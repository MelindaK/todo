var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');
var handlebars = require('handlebars');

var TodoCollection = require('../Collection/TodoCollection.js');
var TodoModel = require('../Model/TodoModel.js');

var todoViewTemplate = require('../templates/todo.hbs');


var TodoView = Backbone.View.extend({
    tagName: 'li',
    className: 'todoContainer',
    events: {
        'keypress .todo': 'updateTodo',
        'click .deleteTodo': 'deleteTodo',
        'click .todoCheckBox': 'markComplete',
    },

    initialize: function(){
        // this.todo = new TodoModel();
        this.render();
    },

    render: function(){
        var todo = this.model.toJSON();
        this.el.innerHTML = todoViewTemplate({subject: todo.subject});
    },

    updateTodo: function(e){
        var code = e.keyCode
        var newSubject = e.currentTarget.value;

        if (code === 13) {
            this.model.save({"subject": newSubject});
            e.currentTarget.blur();
        }
    },

    deleteTodo: function(){

        this.model.destroy();
        this.el.parentNode.removeChild(this.el);
    },

    markComplete: function(){
        this.model.save({"completed": !this.model.get('completed')});

    },
})

module.exports = TodoView;
