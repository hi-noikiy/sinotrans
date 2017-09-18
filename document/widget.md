# 日历控件

django admin site 专门使用一套 jQuery 为了不会和其它 jQuery 干扰，使用方式与一般$开头不同，是django.jQuery。
如果页面本身就已经引入了 jQuery，那么只需要在 jquery.init.js 上修改一下即可，否则请直接引入 admin site 的 jQuery 库。
``` javascript
<script src="{% static 'admin/js/jquery.js' %}"></script>
<script src="{% static 'admin/js/jquery.init.js' %}"></script>
```

jquery.init.both.js
``` javascript
var django = {
    "jQuery": jQuery.noConflict(true)
};
var jQuery = django.jQuery;
var $=jQuery;
```

目前Jquery.init.js里是下面这个，能正常工作
``` javascript
var django = django || {};
django.jQuery = jQuery.noConflict(true);
```

参考
- [在 Django admin site 之外使用其日历控件](http://blog.xavierskip.com/2016-10-22-django-admit-calendar-widget/)
- [将django 管理端的时间控件用于前端](https://www.douban.com/note/350934079/)
https://stackoverflow.com/questions/38601/using-django-time-date-widgets-in-custom-form
