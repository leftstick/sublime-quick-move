/**
 *  Defines the $name controller
 *
 *  @author  $user
 *  @date    $date
 *
 */
(function(define) {
    "use strict";

    /**
     * Register the $name class with RequireJS
     */
    define([],

        function() {

            /**
             * Constructor function used by AngularJS to create instances of this controller.
             *
             * @constructor
             */
            var $name = function($$scope, $$state, $$translate) {

            };

            //Expose this controller definition as a RequireJS module
            //Note: specify the inline annotation explicity
            return ["$$scope", "$$state", '$$translate', $name];

        });


})(define);
