Router.configure({
	layoutTemplate: 'main'
});

Router.route('/', function() {
  this.render('landing');
});

Router.route('/view_image/:username', function () {
	this.render("view_image", {
		data: function() { return this.params.username}
	});
});
