var Backbone = require('backbone');

var ItemModel = Backbone.Model.extend({
    defaults: {
        part1: 'hello',
        part2: 'world'
    }
});

module.exports = ItemModel;
