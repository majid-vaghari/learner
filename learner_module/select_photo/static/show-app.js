var myApp = angular.module('myApp', ['cfp.hotkeys']);

myApp.controller('mycontroller', ['$scope', '$timeout', '$http', 'hotkeys', function ($scope, $timeout, $http, hotkeys) {

    $scope.finished = false;
    $scope.current = {};

    $scope.nextPic = function () {
        console.log($scope.picId);
        $scope.picId = $scope.nextId;
        $http.get('/next/c/' + $scope.picId)
            .success(function (result) {
                if (result.nextId != 'null')
                    $scope.nextId = result.nextId;
                else
                    $scope.finished = true;
            });
    };

    $scope.getData = function () {
        $http.get('/get/' + $scope.picId)
            .success(function (result) {
                $scope.current.id = result.id;
                $scope.current.cat = result.category;
                $scope.current.l1 = result.label1;
                $scope.current.l2 = result.label2;
                $scope.current.l3 = result.label3;
                $scope.current.cmp = result.completed;
            });
    };


    $timeout(function () {
        $scope.getData();
    }, 0);


    $scope.skip = function () {
        $scope.nextPic();
        $scope.getData();
    };


    hotkeys.add({
        combo: 'enter',
        callback: function () {
            $scope.skip();
        }
    });
    hotkeys.add({
        combo: 'space',
        callback: function () {
            $scope.skip();
        }
    });
}]);