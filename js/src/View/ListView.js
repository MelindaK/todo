var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');

var ItemCollection = require('../Collection/ItemCollection.js');
var ItemModel = require('../Model/ItemModel.js');
var ItemView = require('./ItemView.js');

var ListView = Backbone.View.extend({
    el: $('body'),

    events: {
        'click button#add': 'addItem',
    },

    initialize: function() {
        _.bindAll(this, 'render', 'addItem', 'appendItem');

        this.collection = new ItemCollection();

        this.collection.bind('add', this.appendItem);

        this.counter = 0;
        this.render();
    },

    render: function() {
        var self = this;
        $(this.el).append("<button id='add'>Add list item</button>");
        $(this.el).append("<ul></ul>");
        _(this.collection.models).each(function(item) {
            self.appendItem(item);
        }, this);
    },

    addItem: function() {
        this.counter++;
        var item = new ItemModel();
        item.set({
            part2: item.get('part2') + this.counter
        });
        this.collection.add(item);
    },

    appendItem: function(item) {
        var itemView = new ItemView({
            model: item
        });
        $('ul', this.el).append(itemView.render().el);
    }
});

module.exports = ListView;
