import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Comparator;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
//import org.apache.hadoop.mapreduce.Comparator;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;

public class Sortndes {
  public static class TokenizerMapper
       extends Mapper<Object, Text, LongWritable, Text>{

    //private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
    @Override
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      String batsman_bowler = itr.nextToken();
      String run=itr.nextToken();
      int temp=Integer.parseInt(run);
      String null_char =new String(" ");
      String pair;
     /* if(temp<10)
      {
          pair=new String("1"+"_"+run+"_"+batsman_bowler);
      }
      else if(temp>=100)
      {
          pair=new String("3"+"_"+run+"_"+batsman_bowler);
      }
      else
      {
          pair=new String("2"+"_"+run+"_"+batsman_bowler);
      }*/
      context.write(new LongWritable(temp),new Text(batsman_bowler));
  }
}

  public static class IntSumReducer
       extends Reducer<LongWritable,Text,LongWritable,Text> {
    private LongWritable result = new LongWritable();

    public void reduce(LongWritable key,Iterable<Text> values,
                       Context context
                       ) throws IOException, InterruptedException {
     // int sum = 0;
      for (Text val : values){
        //sum += val.get();
        context.write(key,new Text(val));
}
      //String null_char =new String(" ");
      //result.set(sum);
      //context.write(key,new Text(null_char));
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(Sortndes.class);
    job.setSortComparatorClass(LongWritable.DecreasingComparator.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(LongWritable.class);
    job.setOutputValueClass(Text.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
