'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

sass.compiler = require('node-sass');

gulp.task('sass', function () {
    return gulp.src('<app_name>/**/*.scss')
        .pipe(sass())
        .pipe(gulp.dest(function (f) {
            return f.base;
        }));
});

gulp.task('default', function () {
    gulp.watch('<app_name>/**/*.scss', gulp.series('sass'));
});
