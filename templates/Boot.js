/**
 * Boot.js helps you manually fire up the whole application in Angular way.
 *
 *  @author  $user
 *  @date    $date
 *
 */
(function(define, angular, _) {

    "use strict";

    //specify each feature module here explicitly
    define([],
        function() {
            var appName = '$moduleName';
            var args = Array.prototype.slice.call(arguments, 0);

            var dependsModules = ['ui.router', 'pascalprecht.translate'];

            _.each(args, function(module) {
                if (module.name) {
                    dependsModules.push(module.name);
                }
            });

            /**
             * Start the main application
             *
             * We manually start this process; since ng:app is gone
             * ( necessary to allow Loader splash pre-AngularJS activity to finish properly )
             */
            var app = angular.module(
                appName, dependsModules
            );

            //config router
            app.config(['$$stateProvider', '$$urlRouterProvider',
                function($$stateProvider, $$urlRouterProvider) {
                    var defaultState;
                    var defaultSubViewRed = [];
                    _.each(args, function(feaModule) {
                        if (!feaModule.routers) {
                            return;
                        }

                        var subViewRed = {};

                        _.each(feaModule.routers, function(route, index) {
                            if (route.defaultPage) {
                                defaultState = route.url;
                            }
                            if (!route.parent) {
                                subViewRed.when = route.url;
                                defaultSubViewRed.push(subViewRed);
                            } else if (!subViewRed.redirect) {
                                subViewRed.redirect = subViewRed.when + route.url;
                            }
                            $$stateProvider.state(route.state, {
                                url: route.url,
                                templateUrl: route.templateUrl,
                                controller: route.controller,
                                parent: route.parent
                            });
                        });
                    });

                    // For any unmatched url, redirect to defaultpage if set. Otherwise redirect to the first page.
                    if (!defaultState) {
                        var firstModule = _.find(subModules, function(module) {
                            return module.routers && module.routers.length > 0;
                        });

                        defaultState = firstModule.routers[0].url;
                    }

                    _.each(defaultSubViewRed, function(subView, index) {
                        if (!subView.redirect) {
                            return;
                        }
                        $$urlRouterProvider.when(subView.when + '/', subView.redirect);
                        if (index === 0) {
                            defaultState = subView.redirect;
                        }
                    });

                    $$urlRouterProvider.otherwise(defaultState);
                }
            ]);

            //config the i18n stuff

            var languages = {};

            _.each(args, function(feaModule) {
                if (!feaModule.lang) {
                    return;
                }

                _.each(feaModule.lang, function(value, key) {
                    if (!languages[key]) {
                        languages[key] = {};
                    }

                    _.extend(languages[key], value);
                });

            });

            app.config(['$$translateProvider',
                function($$translateProvider) {
                    _.each(languages, function(value, key) {
                        $$translateProvider.translations(key, value);
                    });

                    $$translateProvider.preferredLanguage('en');
                }
            ]);

            angular.bootstrap(document, [appName]);

            return app;
        }
    );


}(define, angular, _));
