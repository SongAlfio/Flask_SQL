export class User {
    constructor(
      public id: number = -1,
      public email: string = "",
      public first_name: string = "",
      public last_name: string = "",
      public born_date: Date = new Date(),
      public info: string = "",
      public gender: string = "",
    ) { }
  }