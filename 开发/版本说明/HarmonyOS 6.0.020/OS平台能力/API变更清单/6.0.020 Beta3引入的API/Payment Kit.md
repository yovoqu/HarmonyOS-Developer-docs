# Payment Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-paymentkit-6003

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global； API声明：declare namespace thirdPaymentService 差异内容：declare namespace thirdPaymentService | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：thirdPaymentService； API声明：class ThirdPayClient 差异内容：class ThirdPayClient | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：ThirdPayClient； API声明：handlePayCallback(want: Want): boolean; 差异内容：handlePayCallback(want: Want): boolean; | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：ThirdPayClient； API声明：pay(payInfo: string): Promise<void>; 差异内容：pay(payInfo: string): Promise<void>; | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：thirdPaymentService； API声明：enum PayMethod 差异内容：enum PayMethod | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：PayMethod； API声明：WECHAT_PAY = 'wechat_pay' 差异内容：WECHAT_PAY = 'wechat_pay' | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：PayMethod； API声明：ALI_PAY = 'ali_pay' 差异内容：ALI_PAY = 'ali_pay' | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增API | NA | 类名：PayMethod； API声明：WECHAT_MINI_PROGRAM = 'wechat_mini_program' 差异内容：WECHAT_MINI_PROGRAM = 'wechat_mini_program' | api/@hms.core.payment.thirdPaymentService.d.ts |
| 新增kit | 类名：global； API声明： 差异内容：NA | 类名：global； API声明：api@hms.core.payment.thirdPaymentService.d.ts 差异内容：PaymentKit | api/@hms.core.payment.thirdPaymentService.d.ts |
