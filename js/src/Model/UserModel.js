var Backbone = require('backbone');

var UserModel = Backbone.Model.extend({
    url: '/me',
    parse: function(response){
        return response.result;
    }

})

module.exports = UserModel;
