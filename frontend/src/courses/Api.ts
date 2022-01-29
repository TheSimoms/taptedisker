export interface CoursesResponse {
  count: number;
  next: string;
  previous: string;
  results: CourseList[];
}

export interface CourseList {
  name: string;
  slug: string;
  image: string;
}

export interface CourseDetails extends CourseList {
  longitude: number;
  latitude: number;
}
