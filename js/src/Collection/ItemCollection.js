var Backbone = require('backbone');

var ItemModel = require('../Model/ItemModel.js');

var ItemCollection = Backbone.Collection.extend({
    model: ItemModel
});

module.exports = ItemCollection;
