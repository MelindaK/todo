var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');

var ItemView = Backbone.View.extend({
    tagName: 'li',

    initialize: function() {
        _.bindAll(this, 'render');
    },

    render: function() {
        $(this.el).html('<span>' + this.model.get('part1') + ' ' +
                this.model.get('part2') + '</span>' + ' <button class="swap">Swap!</button>' + ' <button class="delete">Delete!</button>');
        return this;
    },

    events: {
        'click button.swap': 'swapItems',
        'click button.delete': 'deleteItem'
    },

    swapItems: function() {
        this.model.set({part1: this.model.get('part2'), part2: this.model.get('part1')});
        this.render();
    },

    deleteItem: function() {
        this.model.destroy();
        this.el.parentNode.removeChild(this.el);
    }
});

module.exports = ItemView;
