/**
 * System config
 * define all paths with require js, this is the main entrance of the application which required by Achilles.
 *
 *  @author  $user
 *  @date    $date
 *
 */
(function(require, $$, _) {

    var bizBase = require.toUrl('business');
    var baseUrl = bizBase + '/js';
    require.config({
        paths: {
            'js': baseUrl
        }
    });


    define([
        'js/Bootstrap'
    ], function() {

    });

}(require, $$, _));
