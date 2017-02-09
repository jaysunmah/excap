var casper = require('casper').create();

casper.start('http://casperjs.org/', function() {
    this.echo(this.getTitle());
	this.capture("a.png");
});

casper.run();
