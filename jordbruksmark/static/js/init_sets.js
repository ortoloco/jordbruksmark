
define([], function () {
	var table = $('#filter-table').DataTable( {
	"paging":   false,
	"info":     false,
	"search": {
		"regex": true,
		"smart": false
  	},
	fixedHeader: true,
	});
});
