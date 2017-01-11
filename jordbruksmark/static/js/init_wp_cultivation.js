/*global define */
define([], function () {

    $('#list').load('wp_cultivation/1/');

    $('#week_select').change(function () {
	$('#list').load('wp_cultivation/'+this.value+'/');
     });
});
