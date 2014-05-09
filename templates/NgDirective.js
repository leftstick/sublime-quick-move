/**
 *  A $name directive which helps you...
 *
 *
 *  Usages:
 *
 *      <$dir ></$dir>
 *
 *
 *  @author  $user
 *  @date    $date
 *
 */
(function(define, angular) {
    "use strict";

    /**
     * Register the $name class with RequireJS
     *
     */
    define([],

        function() {

            /**
             * Constructor function used by AngularJS to create instances of this directive.
             *
             * @constructor
             */
            var $name = function() {

                // Return configured, directive instance
                return {
                    restrict: 'AE',
                    transclude: true,
                    scope: {},
                    link: function($$scope, element, attrs) {

                    },
                    template: ''
                };
            };

            // Publish the $name directive construction function
            //Note: specify the inline annotation explicity
            return [$name];

        });

})(define, angular);
