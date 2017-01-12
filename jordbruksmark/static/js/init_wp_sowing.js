/*global define */
define([], function () {

    $('#list').load('wp_sowing/1/');

    $('#week_select').change(function () {
	$('#list').load('wp_sowing/'+this.value+'/');
     });
});
