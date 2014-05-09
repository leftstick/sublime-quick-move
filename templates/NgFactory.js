/**
 *
 *   Defines the $name factory
 *
 *
 *  @author  $user
 *  @date    $date
 */
(function(define) {
    "use strict";

    define([],

        function() {

            var $name = function() {

                var factory = {};

                //This might be modified by yourself
                factory.getSomething = function() {

                };

                return factory;

            };

            //Expose this factory definition as a RequireJS module
            //Note: specify the inline annotation explicity
            return [$name];

        });

}(define));
