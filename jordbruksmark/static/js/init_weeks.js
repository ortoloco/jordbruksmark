/*global define */
define([], function () {
    $('.week_input').change(function () {
	$.get('updateweek/'+$(this).attr('id')+'/'+$(this).val());
     });
});
