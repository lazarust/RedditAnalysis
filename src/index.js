import 'htmx.org';
import './main.css';
import $ from 'jquery';
import 'select2';                

$(() => {
    $('.subreddit-select').select2();
  });

window.addEventListener("DOMContentLoaded", (e) => {
  $('select').on('select2:select', function (e) {
      $(this).closest('select').get(0).dispatchEvent(new Event('change'));
  });
});

window.addEventListener("DOMContentLoaded", (e) => {
  $('body').on('keyup', '.select2-search__field', function() {
    var value = this.value;
    console.log(value);
    $.ajax('/search-subs/?' + $.param({text: value}))
  });
});

