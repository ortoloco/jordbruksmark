/*global define */
define([], function () {

    $('#list').load('wp_plant/1/');

    $('#week_select').change(function () {
	$('#list').load('wp_plant/'+this.value+'/');
     });
});
