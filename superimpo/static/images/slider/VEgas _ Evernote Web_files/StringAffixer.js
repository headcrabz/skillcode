/**
 * Copyright 2015 Evernote Corporation. All rights reserved.
 */

/**
 * A collection of methods that add prefixes or suffixes to strings. Useful for cases such
 * as repetitively constructing CSS strings that must be prefixed by some value.
 */
define([],function() {
  return {
    /**
     * Gets a closure that prefixes a list of strings with some CSS prefix. The resulting
     * list is separated by spaces, and includes the prefix as its own class name at the
     * start of the string.
     *
     * For example, if you created a closure with a prefix of "MyModule", and you passed
     * in an array containing "foo" and "bar" to the closure, then the closure would
     * return the string "MyModule MyModule-foo MyModule-bar". And similarly, if you
     * provided an empty list to the closure, the resulting string would simply be the
     * prefix, "MyModule".
     *
     * This is useful for namespacing your CSS, and to easily style HTML elements
     * (e.g. h1, p, button) without bleeding styles to other modules.
     *
     * @param {string} cssPrefix  a prefix to add to each provided CSS class name
     * @return {function(): string} a closure that can take a variable list of strings
     *     (we use "arguments" to access the parameters) and returns a single class string
     */
    getCssPrefixer: function(cssPrefix) {
      return function() {
        var classNames = Array.prototype.slice.call(arguments);
        return classNames.reduce(function(previousClasses, currentClass) {
          return previousClasses + ' ' + cssPrefix + '-' + currentClass;
        }, cssPrefix);
      };
    },

    getI18nPrefixer: function(i18nPrefix) {
      return function(key) {
        return i18nPrefix + '.' + key;
      };
    }
  };
});
