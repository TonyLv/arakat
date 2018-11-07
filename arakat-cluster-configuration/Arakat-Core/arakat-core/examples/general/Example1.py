from pipeline_generator.generators import PipelineGenerator

data={
    "graph":{
        "nodes": {
            "node1":
                {
                    "id": "node1",
                    "name": "Batch Read from CSV",
                    "category": 0,
                    "parent": "task1",
                    "node_id": 47,
                    "node_type": 0,
                    "family": 0,
                    "compatible_with_stream": False,
                    "compatible_stream_output_modes": [],
                    "compatible_with_spark_pipeline": False,
                    "is_splitter": False,
                    "produces_model": False,
                    "can_infer_schema": True,
                    "file_type": "csv",
                    "parameters": {
                        "path": {"value": "file:///usr/local/spark_code/train.csv", "type": "string"},
                        "header": {"value": True, "type": "boolean"},
                        "sep": {"value": ",", "type": "string"},
                        "quote": {"value": '\\\"', "type": "string"}
                    },
                    "df_constraints": []
                },
            "node2":
                {
                    "id": "node2",
                    "parent": "task1",
                    "node_id": 61,
                    "name": "Batch Write to Parquet",
                    "category": 1,
                    "node_type": 0,
                    "family": 2,
                    "compatible_with_stream": False,
                    "compatible_stream_output_modes": [],
                    "compatible_with_spark_pipeline": False,
                    "is_splitter": False,
                    "produces_model": False,
                    "file_type": "parquet",
                    "parameters": {
                        "path": {"value": "hdfs://namenode:9000/example1/", "type": "string"}
                    },
                    "df_constraints": []
                },
            "task1": {
                "id": "task1",
                "parent": None,
                "node_type": 1
            }
        },
        "edges": {"node1-node2": {"type": "dataframe"}}
    },
    "dag_properties": {
        "app_id": "MyFirstApp",
        "code_base_path": "path_to_put_spark_scripts",
        "schedule_interval": "@once",
        "default_args": {
            "owner": "airflow",
            "start_date": "01/01/2018"
        },
        "spark_operator_conf": {
            "conn_id": "spark_con_py",
            "depends_on_past": False,
            "conf": {"spark.pyspark.python": "/usr/bin/python2.7"}
        }
    }
}

code_info, success, errors, additional_info = PipelineGenerator.generate_pipeline(data["graph"], data["dag_properties"])