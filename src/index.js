import 'htmx.org';
import './main.scss';
import $ from 'jquery';
import 'select2';                

$(() => {
    $('.subreddit-select').select2({
      ajax: {
        url: '/api/search-subs',
        dataType: 'json'
      },
      dropdownCssClass: ':all:',
      selectionCssClass: ':all:',
    });
});

window.addEventListener("DOMContentLoaded", (e) => {
  $('select').on('select2:select', function (e) {
      $(this).closest('select').get(0).dispatchEvent(new Event('change'));
      $('.charts').empty();
  });
});
