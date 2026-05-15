# Calendar Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-calendarkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>; 差异内容：ohos.permission.WRITE_CALENDAR | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void; 差异内容：ohos.permission.WRITE_CALENDAR | 类名：CalendarManager； API声明：createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar): Promise<void>; 差异内容：ohos.permission.WRITE_CALENDAR | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar): Promise<void>; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void; 差异内容：ohos.permission.WRITE_CALENDAR | 类名：CalendarManager； API声明：deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void; 差异内容：ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>; 差异内容：ohos.permission.READ_CALENDAR | 类名：CalendarManager； API声明：getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void; 差异内容：ohos.permission.READ_CALENDAR | 类名：CalendarManager； API声明：getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getCalendar(callback: AsyncCallback<Calendar>): void; 差异内容：ohos.permission.READ_CALENDAR | 类名：CalendarManager； API声明：getCalendar(callback: AsyncCallback<Calendar>): void; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getAllCalendars(): Promise<Calendar[]>; 差异内容：ohos.permission.READ_CALENDAR | 类名：CalendarManager； API声明：getAllCalendars(): Promise<Calendar[]>; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
| 权限变更 | 类名：CalendarManager； API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void; 差异内容：ohos.permission.READ_CALENDAR | 类名：CalendarManager； API声明：getAllCalendars(callback: AsyncCallback<Calendar[]>): void; 差异内容：ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR | api/@ohos.calendarManager.d.ts |
