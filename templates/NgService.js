/**
 *
 *   Defines the $name service
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

                //This might be modified by yourself
                this.getSomething = function() {

                };

            };

            //Expose this service definition as a RequireJS module
            //Note: specify the inline annotation explicity
            return [$name];

        });

}(define));
