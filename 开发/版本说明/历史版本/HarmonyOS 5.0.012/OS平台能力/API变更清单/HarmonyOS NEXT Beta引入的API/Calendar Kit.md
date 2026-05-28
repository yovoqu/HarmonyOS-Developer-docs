# Calendar Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-calendarkit-b065

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount): Promise&lt;Calendar&gt;; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount): Promise&lt;Calendar&gt;; 差异内容：ohos.permission.WRITE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback&lt;Calendar&gt;): void; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback&lt;Calendar&gt;): void; 差异内容：ohos.permission.WRITE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar): Promise&lt;void&gt;; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar): Promise&lt;void&gt;; 差异内容：ohos.permission.WRITE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback&lt;void&gt;): void; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback&lt;void&gt;): void; 差异内容：ohos.permission.WRITE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getCalendar(calendarAccount?: CalendarAccount): Promise&lt;Calendar&gt;; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | 类名：CalendarManager； API声明：getCalendar(calendarAccount?: CalendarAccount): Promise&lt;Calendar&gt;; 差异内容：ohos.permission.READ_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback&lt;Calendar&gt;): void; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | 类名：CalendarManager； API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback&lt;Calendar&gt;): void; 差异内容：ohos.permission.READ_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getCalendar(callback: AsyncCallback&lt;Calendar&gt;): void; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | 类名：CalendarManager； API声明：getCalendar(callback: AsyncCallback&lt;Calendar&gt;): void; 差异内容：ohos.permission.READ_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getAllCalendars(): Promise<Calendar[]>; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | 类名：CalendarManager； API声明：getAllCalendars(): Promise<Calendar[]>; 差异内容：ohos.permission.READ_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | 类名：CalendarManager； API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void; 差异内容：ohos.permission.READ_CALENDAR | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule； API声明：daysOfWeek?: number[]; 差异内容：daysOfWeek?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule； API声明：daysOfMonth?: number[]; 差异内容：daysOfMonth?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule； API声明：daysOfYear?: number[]; 差异内容：daysOfYear?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule； API声明：weeksOfMonth?: number[]; 差异内容：weeksOfMonth?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule； API声明：weeksOfYear?: number[]; 差异内容：weeksOfYear?: number[]; | api/@ohos.calendarManager.d.ts |
| 新增API | NA | 类名：RecurrenceRule； API声明：monthsOfYear?: number[]; 差异内容：monthsOfYear?: number[]; | api/@ohos.calendarManager.d.ts |
