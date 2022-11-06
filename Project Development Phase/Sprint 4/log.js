var myApp = angular.module('logoutApp',[]);

myApp.controller('logoutController', ['$scope', '$interval', '$location', function($scope, $interval, $location) {
  $scope.seconds = 5;
  $scope.loadingShowed = true;
  $interval(function() {
    $scope.seconds--;
    if ($scope.seconds<=0) {
      $scope.loadingShowed = false;
       $scope.redirect();
    }
  }, 1000, 5);
  $scope.redirect = function(){
    $location.path('/full');
  }
}]);