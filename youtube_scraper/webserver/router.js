Router.configure({
	layoutTemplate: 'main'
});

Router.route('/', function() {
  this.render('landing');
});

Router.route('/projects', function() {
  this.render('projects');
});

Router.route('/admin/console', function() {
  this.render('console');
});
