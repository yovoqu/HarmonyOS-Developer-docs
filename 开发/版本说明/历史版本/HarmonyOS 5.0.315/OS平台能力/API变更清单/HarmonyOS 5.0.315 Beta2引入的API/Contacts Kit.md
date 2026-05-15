# Contacts Kit

更新时间：2026-01-21 11:07:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-contactskit-5032

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：contact； API声明：function addContactViaUI(context: Context, contact: Contact): Promise<number>; 差异内容：function addContactViaUI(context: Context, contact: Contact): Promise<number>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明：function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>; 差异内容：function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionOptions； API声明：maxSelectable?: number; 差异内容：maxSelectable?: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionOptions； API声明：isDisplayedByName?: boolean; 差异内容：isDisplayedByName?: boolean; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionOptions； API声明：filter?: ContactSelectionFilter; 差异内容：filter?: ContactSelectionFilter; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： interface ContactSelectionFilter 差异内容： interface ContactSelectionFilter | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionFilter； API声明：filterClause: FilterClause; 差异内容：filterClause: FilterClause; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSelectionFilter； API声明：filterType: FilterType; 差异内容：filterType: FilterType; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： enum FilterType 差异内容： enum FilterType | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterType； API声明：SHOW_FILTER 差异内容：SHOW_FILTER | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterType； API声明：DEFAULT_SELECT 差异内容：DEFAULT_SELECT | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterType； API声明：SHOW_FILTER_AND_DEFAULT_SELECT 差异内容：SHOW_FILTER_AND_DEFAULT_SELECT | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： interface FilterClause 差异内容： interface FilterClause | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterClause； API声明：id?: Array<FilterOptions>; 差异内容：id?: Array<FilterOptions>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterClause； API声明：name?: Array<FilterOptions>; 差异内容：name?: Array<FilterOptions>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterClause； API声明：dataItem?: DataFilter; 差异内容：dataItem?: DataFilter; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterClause； API声明：focusModeList?: Array<FilterOptions>; 差异内容：focusModeList?: Array<FilterOptions>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： interface FilterOptions 差异内容： interface FilterOptions | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterOptions； API声明：filterCondition: FilterCondition; 差异内容：filterCondition: FilterCondition; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterOptions； API声明：value?: string \| ValueType[]; 差异内容：value?: string \| ValueType[]; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： enum FilterCondition 差异内容： enum FilterCondition | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterCondition； API声明：IS_NOT_NULL 差异内容：IS_NOT_NULL | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterCondition； API声明：EQUAL_TO 差异内容：EQUAL_TO | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterCondition； API声明：NOT_EQUAL_TO 差异内容：NOT_EQUAL_TO | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterCondition； API声明：IN 差异内容：IN | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterCondition； API声明：NOT_IN 差异内容：NOT_IN | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：FilterCondition； API声明：CONTAINS 差异内容：CONTAINS | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： interface DataFilter 差异内容： interface DataFilter | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：DataFilter； API声明：field: DataField; 差异内容：field: DataField; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：DataFilter； API声明：options: Array<FilterOptions>; 差异内容：options: Array<FilterOptions>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact； API声明： enum DataField 差异内容： enum DataField | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：DataField； API声明：EMAIL 差异内容：EMAIL | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：DataField； API声明：PHONE 差异内容：PHONE | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：DataField； API声明：ORGANIZATION 差异内容：ORGANIZATION | api/@ohos.contact.d.ts |
