const gulp = require("gulp");
const gap = require("gulp-append-prepend");

gulp.task("licenses", async function () {
  // this is to add mapche licenses in the production mode for the minified js
  gulp
    .src("dist/js/*.js", { base: "./" })
    .pipe(
      gap.prependText(`/*!

=========================================================
* mapche - v1.1.0 based on mapche by mapche
=========================================================

* Product Page: https://www.mapche.com
* Copyright 2022 mapche (https://www.mapche.com)
* Coded by mapche

=========================================================

* The above copyright notice and shall be included in all copies or substantial portions of the Software.

*/`)
    )
    .pipe(gulp.dest("./", { overwrite: true }));

  // this is to add Creative Tim licenses in the production mode for the minified html
  gulp
    .src("dist/index.html", { base: "./" })
    .pipe(
      gap.prependText(`<!--

=========================================================
* mapche - v1.1.0 based on mapche by mapche
=========================================================

* Product Page: https://www.mapche.com
* Copyright 2022 mapche (https://www.mapche.com)
* Coded by mapche

=========================================================

* The above copyright notice and shall be included in all copies or substantial portions of the Software.

-->`)
    )
    .pipe(gulp.dest("./", { overwrite: true }));

  // this is to add Creative Tim licenses in the production mode for the minified css
  gulp
    .src("dist/css/*.css", { base: "./" })
    .pipe(
      gap.prependText(`/*!

=========================================================
* mapche - v1.1.0 based on mapche by mapche
=========================================================

* Product Page: https://www.mapche.com
* Copyright 2022 mapche (https://www.mapche.com)
* Coded by mapche

=========================================================

* The above copyright notice and shall be included in all copies or substantial portions of the Software.

*/`)
    )
    .pipe(gulp.dest("./", { overwrite: true }));
  return;
});
