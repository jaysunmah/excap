Template.view_image.events({
  'click #runScript' (event) {
    var cb = function(error, response) {
      console.log(response);
      Router.go("/view_image/" + $('#username').val());
    }
    Meteor.call("runScript", $('#username').val(), $('#password').val(), cb);
  },
});

Template.view_image.helpers({
  selectedImage: function() {
    var re = /\/view_image\/(.*)/;
    return Router.current().url.match(re)[1] || "";
  },
});

Template.view_image.onRendered(function() {
  console.log("wei");
});
