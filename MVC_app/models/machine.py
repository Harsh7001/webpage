from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the engine and session
engine = create_engine('sqlite:///population_data.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the base model
Base = declarative_base()

# Define the models
class SamplePop(Base):
    __tablename__ = 'sample_pop'
    id = Column(Integer, primary_key=True)
    population = Column(String)

class Populations(Base):
    __tablename__ = 'Populations'
    superpopulation_code = Column(String, primary_key=True)
    superpopulation_name = Column(String)
    population_code = Column(String, ForeignKey('sample_pop.population'))
    population_name = Column(String)

class GeneticData(Base):
    __tablename__ = 'genetic_data'
    id = Column(String, primary_key=True)
    chrom = Column(String)
    chrom_pos = Column(Integer)
    genotype = Column(Integer)
    sample_pop_id = Column(Integer, ForeignKey('sample_pop.id'))

class SNP(Base):
    __tablename__ = 'SNP'
    chrom_position = Column(Integer, primary_key=True)
    gene_name = Column(String)
    clinical_relevance = Column(String)
    genetic_data_chrom_pos = Column(Integer, ForeignKey('genetic_data.chrom_pos'))

class ClusteringAnalysis(Base):
    __tablename__ = 'clustering_analysis'
    id = Column(String, primary_key=True)
    PCA_1 = Column(Integer)
    PCA_2 = Column(Integer)
    sample_pop_id = Column(Integer, ForeignKey('sample_pop.id'))

class Admixture(Base):
    __tablename__ = 'admixture'
    id = Column(String, primary_key=True)
    P1 = Column(Integer)
    P2 = Column(Integer)
    P3 = Column(Integer)
    P4 = Column(Integer)
    P5 = Column(Integer)
    sample_pop_id = Column(Integer, ForeignKey('sample_pop.id'))

# Create the tables
Base.metadata.create_all(engine)

# Commit changes and close the session
session.commit()
session.close()
